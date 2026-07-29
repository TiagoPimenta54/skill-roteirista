# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from run_roteirista import run_pipeline

# 1. Create rich, biblically accurate ~1400 word Portuguese script for "A história de Jó" (10 MIN)
script_parts = [
    "[I] Na terra de Uz, vivia um homem chamado Jó, cuja vida era um verdadeiro testemunho de retidão, fé e piedade diante do Criador.",
    "[I] Jó era considerado o homem mais íntegro e sincero de todo o Oriente, temente a Deus e que se desviava completamente do mal.",
    "[V] Ele possuía sete filhos e três filhas, além de milhares de ovelhas, camelos, juntas de bois e jumentas, formando uma grande riqueza.",
    "[I] Todos os dias, Jó oferecia sacrifícios em favor de seus filhos, temendo que em seus corações tivessem pecado contra Deus.",
    "[V] Um dia, os anjos se apresentaram diante do Senhor, e entre eles veio também Satanás, o acusador.",
    "[I] O Senhor perguntou a Satanás: 'Observaste o meu servo Jó? Não há ninguém na terra como ele, íntegro e reto.'",
    "[V] Satanás respondeu com zombaria: 'Acaso Jó teme a Deus de graça? Não cercaste de proteção a ele, sua casa e tudo o que tem?'",
    "[I] 'Estende a mão e toca em tudo o que ele possui, e verás se ele não te amaldiçoará na tua própria face.'",
    "[V] O Senhor disse a Satanás: 'Pois bem, tudo o que ele tem está em teu poder; apenas contra ele não estendas a mão.'",
    "[I] Em um único dia, a tragédia caiu devastadora sobre a vida de Jó como uma tempestade avassaladora.",
    "[V] Mensageiros chegaram correndo para avisar que os sabeus haviam atacado e levado todos os bois e jumentas.",
    "[I] Enquanto o primeiro ainda falava, outro chegou dizendo que o fogo de Deus caira do céu e queimara as ovelhas e os servos.",
    "[V] Um terceiro mensageiro anunciou que os caldeus formaram três bandos e levaram todos os camelos, matando os servos a fio de espada.",
    "[I] Por fim, o golpe mais doloroso: um vento forte veio do deserto e derrubou a casa onde todos os seus dez filhos se banqueteavam.",
    "[V] Todos os seus filhos e filhas morreram instantaneamente sob os escombros daquela casa.",
    "[I] Diante de tamanho sofrimento, Jó se levantou, rasgou o seu manto, rapou a cabeça e prostrou-se em terra em adoração.",
    "[V] Ele declarou as famosas palavras: 'Nu saí do ventre de minha mãe e nu voltarei para lá. O Senhor o deu e o Senhor o tomou; bendito seja o nome do Senhor.'",
    "[I] Em tudo isso, Jó não pecou nem atribuiu a Deus culpa alguma pela tragédia que acabara de abalar a sua vida.",
    "[V] Satanás voltou a se apresentar perante o Senhor, insatisfeito porque Jó permanecia firme na sua integridade.",
    "[I] Disse o acusador: 'Pele por pele! Tudo o que o homem tem dará pela sua vida. Toca-lhe nos ossos e na carne, e amaldiçoará a ti.'",
    "[V] O Senhor permitiu que Satanás afligisse o corpo de Jó, mas ordenou que poupasse a sua vida.",
    "[I] Jó foi acometido de feridas malignas desde a planta dos pés até o alto da cabeça, sentindo dores insuportáveis.",
    "[V] Ele sentou-se na cinza e pegou um caco de cerâmica para raspar suas feridas em busca de algum alívio.",
    "[I] Sua própria esposa, vendo aquela miséria profunda, disse-lhe: 'Ainda reténs a tua integridade? Amaldiçoa a Deus e morre.'",
    "[V] Jó respondeu com sabedoria profunda: 'Falas como uma doida. Aceitaremos o bem de Deus e não aceitaríamos o mal?'",
    "[I] Três amigos de Jó — Elifaz, Bildade e Zofar — souberam do desastre e vieram de longe para consolá-lo e chorar com ele.",
    "[V] Ao verem Jó de longe, mal o reconheceram de tão desfigurado. Choraram alto, rasgaram seus mantos e lançaram pó sobre a cabeça.",
    "[I] Durante sete dias e sete noites, sentaram-se com ele na terra em silêncio absoluto, pois viam quão grande era a sua dor.",
    "[V] Quando Jó finalmente abriu a boca, ele lamentou o dia do seu nascimento, expressando a profunda angústia de sua alma.",
    "[I] Seus amigos começaram a argumentar que tamanha dor só poderia ser fruto de algum pecado secreto e grave cometido por Jó.",
    "[V] Elifaz defendeu que os inocentes não perecem e incentivou Jó a buscar o favor de Deus e confessar suas falhas.",
    "[I] Bildade afirmou que a justiça divina é inflexível e que os filhos de Jó deviam ter pecado para merecer tal sorte.",
    "[V] Zofar acusou Jó de arrogância, dizendo que ele falava demais e tentando provar que a sabedoria divina era inalcançável.",
    "[I] Jó defendeu firmemente sua inocência diante das acusações injustas dos amigos, reafirmando que não havia maldade em suas mãos.",
    "[V] Ele clamava por um mediador entre ele e Deus, alguém que pudesse interceder por sua causa perante o Altíssimo.",
    "[I] Em meio ao desespero, Jó proclamou uma das maiores profecias de esperança das Escrituras Sagradas.",
    "[V] Ele declarou: 'Eu sei que o meu Redentor vive, e que por fim se levantará sobre a terra!'",
    "[I] 'E depois de destruída a minha pele, contudo ainda em minha carne verei a Deus, a quem eu mesmo verei com os meus olhos.'",
    "[V] Um jovem chamado Eliú permaneceu escutando o debate em silêncio e finalmente falou, queimando de ira contra Jó e seus amigos.",
    "[I] Eliú destacou a majestade e a soberania inquestionável de Deus, afirmando que o Criador ensina o homem através da aflição.",
    "[V] De repente, o cenário mudou drasticamente: o céu se escureceu e um redemoinho poderoso se formou sobre a terra.",
    "[I] Do meio do redemoinho, a própria voz de Deus respondeu a Jó com perguntas majestosas sobre a criação do universo.",
    "[V] O Senhor perguntou: 'Onde estavas tu quando eu fundava a terra? Faze-me saber, se tens inteligência.'",
    "[I] 'Quem determinou as suas medidas? Ou quem estendeu sobre ela a linha de medir?'",
    "[V] Deus falou das estrelas, das constelações, do mar e das criaturas imponentes como o Behemoth e o Leviatã.",
    "[I] Diante da grandeza inefável do Criador, Jó compreendeu a limitação humana e a soberania absoluta do Senhor.",
    "[V] Jó respondeu ao Senhor: 'Bem sei eu que tudo podes, e que nenhum dos teus pensamentos pode ser impedido.'",
    "[I] 'Antes eu te conhecia só de ouvir falar, mas agora os meus olhos te veem. Por isso me abomino e me arrependo no pó e na cinza.'",
    "[V] O Senhor manifestou sua ira contra os três amigos de Jó, porque não haviam falado o que era reto como o Seu servo Jó.",
    "[I] Deus ordenou que eles oferecessem sacrifícios e que Jó orasse por eles, prometendo aceitar a oração de Jó.",
    "[V] Quando Jó orou pelos seus amigos, o Senhor mudou a sua sorte e restaurou tudo o que ele havia perdido.",
    "[I] O Senhor abençoou o último estado de Jó mais do que o primeiro, dando-lhe o dobro de tudo o que possuía.",
    "[V] Jó recebeu catorze mil ovelhas, seis mil camelos, mil juntas de bois e mil jumentas em suas fazendas.",
    "[I] Deus concedeu-lhe também mais sete filhos e três filhas, as mulheres mais formosas de toda aquela terra.",
    "[V] Jó viveu ainda cento e quarenta anos, viu seus filhos e os filhos de seus filhos até a quarta geração.",
    "[I] E assim morreu Jó, velho e cheio de dias, vitorioso em sua fé inabalável no Deus Vivo."
]

full_script_text = "\n".join(script_parts)

if __name__ == "__main__":
    result = run_pipeline("A historia de JO, B1 C 10MIN", custom_script_text=full_script_text, generate_real_audio=True)
    print("\nPROMPT GEMINI ONLINE:\n")
    print(result["gemini_instructions"])
