# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from run_roteirista import run_pipeline

script_parts = [
    "Na terra de Uz, vivia um homem chamado Jó, cuja vida era um verdadeiro testemunho de retidão, fé e piedade diante do Criador.",
    "Jó era considerado o homem mais íntegro e sincero de todo o Oriente, temente a Deus e que se desviava completamente do mal.",
    "Ele possuía sete filhos e três filhas, além de milhares de ovelhas, camelos, juntas de bois e jumentas, formando uma grande riqueza.",
    "Todos os dias, Jó oferecia sacrifícios em favor de seus filhos, temendo que em seus corações tivessem pecado contra Deus.",
    "Um dia, os anjos se apresentaram diante do Senhor, e entre eles veio também Satanás, o acusador.",
    "O Senhor perguntou a Satanás: 'Observaste o meu servo Jó? Não há ninguém na terra como ele, íntegro e reto.'",
    "Satanás respondeu com zombaria: 'Acaso Jó teme a Deus de graça? Não cercaste de proteção a ele, sua casa e tudo o que tem?'",
    "'Estende a mão e toca em tudo o que ele possui, e verás se ele não te amaldiçoará na tua própria face.'",
    "O Senhor disse a Satanás: 'Pois bem, tudo o que ele tem está em teu poder; apenas contra ele não estendas a mão.'",
    "Em um único dia, a tragédia caiu devastadora sobre a vida de Jó como uma tempestade avassaladora.",
    "Mensageiros chegaram correndo para avisar que os sabeus haviam atacado e levado todos os bois e jumentas.",
    "Enquanto o primeiro ainda falava, outro chegou dizendo que o fogo de Deus caira do céu e queimara as ovelhas e os servos.",
    "Um terceiro mensageiro anunciou que os caldeus formaram três bandos e levaram todos os camelos, matando os servos a fio de espada.",
    "Por fim, o golpe mais doloroso: um vento forte veio do deserto e derrubou a casa onde todos os seus dez filhos se banqueteavam.",
    "Todos os seus filhos e filhas morreram instantaneamente sob os escombros daquela casa.",
    "Diante de tamanho sofrimento, Jó se levantou, rasgou o seu manto, rapou a cabeça e prostrou-se em terra em adoração.",
    "Ele declarou as famosas palavras: 'Nu saí do ventre de minha mãe e nu voltarei para lá. O Senhor o deu e o Senhor o tomou; bendito seja o nome do Senhor.'",
    "Em tudo isso, Jó não pecou nem atribuiu a Deus culpa alguma pela tragédia que acabara de abalar a sua vida.",
    "Satanás voltou a se apresentar perante o Senhor, insatisfeito porque Jó permanecia firme na sua integridade.",
    "Disse o acusador: 'Pele por pele! Tudo o que o homem tem dará pela sua vida. Toca-lhe nos ossos e na carne, e amaldiçoará a ti.'",
    "O Senhor permitiu que Satanás afligisse o corpo de Jó, mas ordenou que poupasse a sua vida.",
    "Jó foi acometido de feridas malignas desde a planta dos pés até o alto da cabeça, sentindo dores insuportáveis.",
    "Ele sentou-se na cinza e pegou um caco de cerâmica para raspar suas feridas em busca de algum alívio.",
    "Sua própria esposa, vendo aquela miséria profunda, disse-lhe: 'Ainda reténs a tua integridade? Amaldiçoa a Deus e morre.'",
    "Jó respondeu com sabedoria profunda: 'Falas como uma doida. Aceitaremos o bem de Deus e não aceitaríamos o mal?'",
    "Três amigos de Jó — Elifaz, Bildade e Zofar — souberam do desastre e vieram de longe para consolá-lo e chorar com ele.",
    "Ao verem Jó de longe, mal o reconheceram de tão desfigurado. Choraram alto, rasgaram seus mantos e lançaram pó sobre a cabeça.",
    "Durante sete dias e sete noites, sentaram-se com ele na terra em silêncio absoluto, pois viam quão grande era a sua dor.",
    "Quando Jó finalmente abriu a boca, ele lamentou o dia do seu nascimento, expressando a profunda angústia de sua alma.",
    "Seus amigos começaram a argumentar que tamanha dor só poderia ser fruto de algum pecado secreto e grave cometido por Jó.",
    "Elifaz defendeu que os inocentes não perecem e incentivou Jó a buscar o favor de Deus e confessar suas falhas.",
    "Bildade afirmou que a justiça divina é inflexível e que os filhos de Jó deviam ter pecado para merecer tal sorte.",
    "Zofar acusou Jó de arrogância, dizendo que ele falava demais e tentando provar que a sabedoria divina era inalcançável.",
    "Jó defendeu firmemente sua inocência diante das acusações injustas dos amigos, reafirmando que não havia maldade em suas mãos.",
    "Ele clamava por um mediador entre ele e Deus, alguém que pudesse interceder por sua causa perante o Altíssimo.",
    "Em meio ao desespero, Jó proclamou uma das maiores profecias de esperança das Escrituras Sagradas.",
    "Ele declarou: 'Eu sei que o meu Redentor vive, e que por fim se levantará sobre a terra!'",
    "'E depois de destruída a minha pele, contudo ainda em minha carne verei a Deus, a quem eu mesmo verei com os meus olhos.'",
    "Um jovem chamado Eliú permaneceu escutando o debate em silêncio e finalmente falou, queimando de ira contra Jó e seus amigos.",
    "Eliú destacou a majestade e a soberania inquestionável de Deus, afirmando que o Criador ensina o homem através da aflição.",
    "De repente, o cenário mudou drasticamente: o céu se escureceu e um redemoinho poderoso se formou sobre a terra.",
    "Do meio do redemoinho, a própria voz de Deus respondeu a Jó com perguntas majestosas sobre a criação do universo.",
    "O Senhor perguntou: 'Onde estavas tu quando eu fundava a terra? Faze-me saber, se tens inteligência.'",
    "'Quem determinou as suas medidas? Ou quem estendeu sobre ela a linha de medir?'",
    "Deus falou das estrelas, das constelações, do mar e das criaturas imponentes como o Behemoth e o Leviatã.",
    "Diante da grandeza inefável do Criador, Jó compreendeu a limitação humana e a soberania absoluta do Senhor.",
    "Jó respondeu ao Senhor: 'Bem sei eu que tudo podes, e que nenhum dos teus pensamentos pode ser impedido.'",
    "'Antes eu te conhecia só de ouvir falar, mas agora os meus olhos te veem. Por isso me abomino e me arrependo no pó e na cinza.'",
    "O Senhor manifestou sua ira contra os três amigos de Jó, porque não haviam falado o que era reto como o Seu servo Jó.",
    "Deus ordenou que eles oferecessem sacrifícios e que Jó orasse por eles, prometendo aceitar a oração de Jó.",
    "Quando Jó orou pelos seus amigos, o Senhor mudou a sua sorte e restaurou tudo o que ele havia perdido.",
    "O Senhor abençoou o último estado de Jó mais do que o primeiro, dando-lhe o dobro de tudo o que possuía.",
    "Jó recebeu catorze mil ovelhas, seis mil camelos, mil juntas de bois e mil jumentas em suas fazendas.",
    "Deus concedeu-lhe também mais sete filhos e três filhas, as mulheres mais formosas de toda aquela terra.",
    "Jó viveu ainda cento e quarenta anos, viu seus filhos e os filhos de seus filhos até a quarta geração.",
    "E assim morreu Jó, velho e cheio de dias, vitorioso em sua fé inabalável no Deus Vivo."
]

full_script_text = "\n".join(script_parts)

if __name__ == "__main__":
    result = run_pipeline("A historia de jo, BI 10 min", custom_script_text=full_script_text, generate_real_audio=True, media_mode="I")
    print("\nPROMPT GEMINI ONLINE:\n")
    print(result["gemini_instructions"])
